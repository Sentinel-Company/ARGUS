from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import ipfshttpclient
from neo4j import GraphDatabase
import redis

app = FastAPI(title="ARGUS API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

neo4j_driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "argus_secure_password"))
ipfs_client = ipfshttpclient.connect('/dns/ipfs/tcp/5001/http')
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

class SearchQuery(BaseModel):
    query: str
    limit: int = 20

@app.get("/")
def root():
    return {"service": "ARGUS API", "version": "1.0.0", "status": "operational"}

@app.post("/api/v1/search/person")
def search_person(query: SearchQuery):
    with neo4j_driver.session() as session:
        result = session.run(
            "MATCH (p:Person) WHERE p.name CONTAINS $query RETURN p.name, p.risk_score, p.nationality ORDER BY p.risk_score DESC LIMIT $limit",
            query=query.query, limit=query.limit
        )
        persons = [{"name": r["p.name"], "risk_score": r["p.risk_score"], "nationality": r["p.nationality"]} for r in result]
        return {"results": persons, "count": len(persons)}

@app.get("/api/v1/graph/person/{name}")
def get_person_graph(name: str, depth: int = 2):
    with neo4j_driver.session() as session:
        result = session.run(
            "MATCH path = (p:Person {name: $name})-[*1..$depth]-(related) RETURN path LIMIT 100",
            name=name, depth=depth
        )
        nodes, edges = [], []
        for record in result:
            path = record["path"]
            for node in path.nodes:
                nodes.append({"id": node.id, "labels": list(node.labels), "properties": dict(node)})
            for rel in path.relationships:
                edges.append({"source": rel.start_node.id, "target": rel.end_node.id, "type": rel.type})
        return {"nodes": nodes, "edges": edges}
