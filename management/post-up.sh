#!/bin/bash
echo "=================="
echo "Post up script"
echo "=================="

echo "Seeding Database"
echo "----"

docker exec -it  dev-portfolio-api python scripts/seed_db.py up -y