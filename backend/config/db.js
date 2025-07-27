import mongoose from "mongoose";

const connectDb = async () => {
  try {
    await mongoose.connect(process.env.MONGODB_URL);
    console.log("✅ DB Connected");
  } catch (error) {
    console.log("❌ DB Error:", error.message); // <-- isko add karo
  }
};

export default connectDb;
