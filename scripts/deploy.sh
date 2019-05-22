#!/bin/bash

set -e

G='\033[0;32m'
NC='\033[0m' # No Color
printf "${G}Starting pre-deployment...${NC}\n"
printf "Building JavaScript ->\n"
yarn build

printf "\n${G}JavaScript Build Successful. Deploying...${NC}\n"
gcloud app deploy

printf \n"${G}Deploy Successful!${NC}\n"