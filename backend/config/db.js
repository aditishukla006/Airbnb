import mongoose from 'mongoose';
import dotenv from "dotenv";
dotenv.config();


// console.log("MONGO_URI from .env:", process.env.MONGO_URI);

const connectDb = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URI);
    console.log('DB connected successfully');
  } catch (error) {
    console.log('DB connection error:', error);
  }
};

export default connectDb;
