#! /usr/bin/env bash

COLOR='\033[0;33m' # yellow
NC='\033[0m' # No Color

# Let the DB start, check with simple 'SQL SELECT 1'
echo -e "${COLOR}Checking postgres connection...${NC}"
python ./app/backend_pre_start.py
echo -e "\n"

# Run migrations AKA create correct tables
echo -e "${COLOR}Running migrations...${NC}"
alembic upgrade head
echo -e "\n"

# Create initial data in DB
echo -e "${COLOR}Adding initial data...${NC}"
python ./app/db/initial_data.py
echo -e "\n"
