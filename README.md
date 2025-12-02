# Airbnb Clone

## Overview
A full-stack Airbnb Clone web application that allows users to list, book, and manage rental properties. Built with **React, Tailwind CSS, Vite, Node.js, Express, and MongoDB**.

---
## Features
- User authentication (login/signup) with JWT
- Property listing CRUD operations
- Image uploads with Cloudinary
- Booking management
- User profile management
- Responsive UI with Tailwind CSS

---
## Tech Stack
### Frontend
- React.js
- Vite
- Tailwind CSS
- Axios

### Backend
- Node.js
- Express.js
- MongoDB (Mongoose)
- Cloudinary
- JWT & bcrypt

---
## Project Structure
```
project-root/
├── client/                 # Frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   ├── context/
│   │   └── utils/
│   ├── public/
│   └── package.json
│
├── server/                 # Backend
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── utils/
│   ├── config/
│   ├── server.js
│   └── package.json
│
├── README.md
└── .env
```

---
## Setup Instructions
### Prerequisites
- Node.js
- MongoDB
- Cloudinary account

### Clone Repository
```
git clone https://github.com/virajsharma-glitch/air_bnb-project.git
cd air_bnb-project
```

### Install Dependencies
#### Server
```
cd server
npm install
```

#### Client
```
cd ../client
npm install
```

### Environment Variables
Create a `.env` file in `server/` with:
```
PORT=3000
MONGODB_URI=your_mongo_uri
JWT_SECRET=your_secret
CLOUDINARY_CLOUD_NAME=your_name
CLOUDINARY_API_KEY=your_key
CLOUDINARY_API_SECRET=your_secret
```

---
## Running the Project
### Run Backend
```
cd server
npm start
```

### Run Frontend
```
cd client
npm run dev
```

Backend will run on: `http://localhost:3000`
Frontend will run on: `http://localhost:5173`

---
## API Endpoints
### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/auth/register | Register new user |
| POST | /api/auth/login | Login user |

### Listings
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/listings | Get all listings |
| POST | /api/listings | Create listing |
| PUT | /api/listings/:id | Update listing |
| DELETE | /api/listings/:id | Delete listing |

### Bookings
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/bookings | Create booking |
| GET | /api/bookings/user | Get user bookings |

---
## Testing
- Unit testing for backend controllers
- API integration testing using Postman
- Manual frontend testing in browser

---
## Lessons Learned
- Full-stack development hands-on experience
- API integration & testing workflows
- MVC architecture benefits
- Git version control & Agile practices

---
## Author
**Viraj Sharma**  
Reg No: 202412121  
MSc. Information Technology

---
## License
This project is for educational purposes only.
