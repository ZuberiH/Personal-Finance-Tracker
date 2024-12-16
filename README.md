# Personal Finance Tracker

## Overview
The Personal Finance Tracker is a microservices-based application designed to help users manage their finances effectively. The app supports functionalities such as expense tracking, user authentication, and statistical reporting through a well-defined REST API architecture. This project incorporates containerization, access control, and a cloud-deployed infrastructure.

---

## Features
- **Expense Tracking**: Add, edit, and view expenses categorized by type.
- **User Management**: Secure user authentication and management.
- **Usage Analytics**: Track and display endpoint usage statistics through an administrative API.
- **Cloud Deployment**: Fully containerized application deployed on Docker.
- **Scalability**: Kubernetes-based container orchestration (optional feature).
- **Extendable**: Additional features like Kafka-based event streaming and machine learning integrations are possible.

---

## Microservices Architecture
The application consists of the following services:
1. **User Service**: Handles user authentication and registration.
2. **Expense Service**: Manages expense-related operations such as CRUD operations for expense entries.
3. **Analytics Service**: Collects and reports usage statistics for each API endpoint.

Each service communicates via REST APIs and is containerized for scalability and ease of deployment.

---

## Setup and Installation

### Prerequisites
- Docker and Docker Compose
- Python 3.10+
- Access to a cloud platform (e.g., AWS, DigitalOcean) for deployment
- Kubernetes (optional for orchestration)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd personal-finance-tracker
   ```

2. **Build and Run Services Locally**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   - User Service: `http://localhost:8000`
   - Expense Service: `http://localhost:8001`
   - Admin Dashboard (Usage Statistics): `http://localhost:8002`

4. **Deploy to Cloud**:
   - Use `docker-compose` for simple setups or configure Kubernetes for scalable orchestration.

---

## API Endpoints

### User Service
- `POST /register`: Register a new user.
- `POST /login`: Authenticate and retrieve a JWT token.

### Expense Service
- `GET /expenses`: Retrieve all expenses for a user.
- `POST /expenses`: Create a new expense.
- `PUT /expenses/{id}`: Update an expense.
- `DELETE /expenses/{id}`: Delete an expense.

### Analytics Service
- `GET /analytics`: Retrieve usage statistics for all endpoints.

---

