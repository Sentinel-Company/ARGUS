#!/usr/bin/env python3
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "argus_secure_password"))

with driver.session() as session:
    session.run("CREATE CONSTRAINT person_name IF NOT EXISTS FOR (p:Person) REQUIRE p.name IS UNIQUE")
    session.run("CREATE CONSTRAINT company_name IF NOT EXISTS FOR (c:Company) REQUIRE c.name IS UNIQUE")
    session.run("CREATE INDEX person_risk_score IF NOT EXISTS FOR (p:Person) ON (p.risk_score)")
    print("✓ Schema initialized")

driver.close()
