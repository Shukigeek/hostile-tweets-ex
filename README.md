HOSTILE TWEETS 

connect to a mongo db and fetch all data
convert it do a DataFrame of pandas
adding 3 new columns by the process
and changing the name of TeewtID and Text
saving all in list format and sanding it to endpoint
and deploying al in open shift the getting a url 
to see all data


hostile-tweets-ex/
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── fetcher.py # Mongo fetch logic
│ ├── processor.py # Text Processing logic
│ └── manager.py # Manages fetcher+processor
│
├── data/
│ └── weapons.txt # list of weapons (blacklist)
│
├── infra/ # OpenShift/K8s manifests (yaml files)
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── route.yaml
│ ├── secrets.yaml
│ └── configmap.yaml
│
├── scripts/
│ └── commands.bat #
│
├── Dockerfile
├── requirements.txt
└── README.md
