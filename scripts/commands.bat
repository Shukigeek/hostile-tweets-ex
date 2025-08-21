REM docker build -t hostile-tweets .

REM docker run -d -p 8000:8000 hostile-tweets
REM docker tag hostile-tweets shuki120/hostile-tweets:v2
REM docker push shuki120/hostile-tweets:v2



oc delete deployment hostile-tweets
oc delete scv hostile-tweets
oc delete secrete hostile-tweets
oc delete route hostile-tweets
oc apply -f infra/deployment.yaml
oc apply -f infra/service.yaml
oc apply -f infra/secret.yaml
oc apply -f infra/route.yaml