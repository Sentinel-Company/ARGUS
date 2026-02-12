from celery import Celery
from neo4j import GraphDatabase
import logging

app = Celery('argus', broker='redis://redis:6379/0')
neo4j_driver = GraphDatabase.driver("bolt://neo4j:7687", auth=("neo4j", "argus_secure_password"))
logger = logging.getLogger(__name__)

@app.task
def daily_graph_analysis():
    logger.info("Running daily analysis")
    with neo4j_driver.session() as session:
        result = session.run(
            "MATCH path = (p:Person)-[:OWNS*3..5]->(c:Company) WHERE c.jurisdiction IN ['BVI', 'Cayman Islands', 'Panama'] RETURN p.name, LENGTH(path) as chain_length ORDER BY chain_length DESC LIMIT 100"
        )
        flagged = 0
        for record in result:
            session.run(
                "MATCH (p:Person {name: $name}) MERGE (p)-[:FLAGGED {reason: 'Deep offshore chain', flagged_at: datetime()}]->(:Alert)",
                name=record["p.name"]
            )
            flagged += 1
        logger.info(f"Flagged {flagged} entities")
    return {"flagged_entities": flagged}
