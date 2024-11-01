Vessel Tracking & Analysis Microservices Application
This application is designed to analyse maritime vessel data for use cases like the VAST Challenge 2024 Mini Challenge 2. It leverages a microservices architecture to manage data ingestion, anomaly detection, and vessel-cargo associations, providing insights into shipping activities. The application is built in Python and deployed using Docker and Kubernetes, with a cloud-ready infrastructure that supports scaling, modularity, and flexibility.
Overview of Microservices
1. Vessel Ingestion Service
•	Description: This service handles the ingestion of vessel tracking data, ensuring that raw data is cleaned and stored for use by other services.
•	Expected Input: JSON data with vessel_id, vessel coordinates, speed, timestamp, and other relevant attributes.
•	Output: Processed data is stored in a persistent database, accessible for analysis by other services.
2. Anomaly Detection Service
•	Description: This service analyses vessel movement patterns to detect unusual behaviours, such as unauthorized route deviations or suspicious stops.
•	Expected Input: Vessel movement data from the Vessel Ingestion Service.
•	Output: JSON response with detected anomalies, including anomaly type, vessel ID, and timestamp, stored for future reference.
3. Vessel-Cargo Association Service
•	Description: This service matches vessels to potential cargo types based on historical data, destination, and other metadata.
•	Expected Input: Vessel tracking data and cargo records.
•	Output: A JSON response associating vessels with likely cargo types, which can be used to infer trade patterns and optimize logistics.
Key Technologies
•	Python: Used for developing microservices with REST API endpoints.
•	Docker: Containers package each microservice, ensuring consistency across different environments.
•	Kubernetes: Manages the deployment and scaling of microservices in a cloud or local environment.
•	MongoDB: A NoSQL database for storing vessel data and analysis results, with data persistence across restarts.
•	Git: Source control for tracking code changes and collaboration.
Architecture Principles
The application follows cloud architecture principles such as:
•	Microservices Architecture: Each service performs a specific task, improving modularity, scalability, and fault tolerance.
•	Cloud Readiness: Docker and Kubernetes support deployment in any cloud environment, making it easy to scale and manage resources.
Setup and Deployment
Prerequisites
•	Docker and Docker Compose for local development and testing.
•	Kubernetes for managing deployments in a distributed environment.
•	Git for cloning the repository and managing code.
Installation and Running Locally
1.	Clone the repository:
Copy code
git clone <repository-url>
cd <repository-directory>
2.	Start services with Docker Compose:
Copy code
docker-compose up -d
3.	Access each service at its respective endpoint for testing:
o	Vessel Ingestion Service: http://localhost:<port>/ingest
o	Anomaly Detection Service: http://localhost:<port>/detect
o	Vessel-Cargo Association Service: http://localhost:<port>/associate
Deployment to Kubernetes
•	Each service has a corresponding Kubernetes YAML file for deployment. Apply the deployments to your cluster: 
Copy code
kubectl apply -f kubernetes/vessel-ingestion-deployment.yaml
kubectl apply -f kubernetes/anomaly-detection-deployment.yaml
kubectl apply -f kubernetes/vessel-cargo-association-deployment.yaml
This application showcases a modular and scalable solution for analysing vessel data, with a focus on flexibility, fault tolerance, and cloud readiness. It’s ideal for data-driven maritime insights, supporting both research and operational decision-making.

