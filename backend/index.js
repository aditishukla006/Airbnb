import express from "express"
import dotenv from "dotenv"
import connectDb from "./config/db.js"
import authRouter from "./routes/auth.route.js"
import cookieParser from "cookie-parser"
dotenv.config()
import cors from "cors"
import userRouter from "./routes/user.route.js"
import listingRouter from "./routes/listing.route.js"
import bookingRouter from "./routes/booking.route.js"
let port = 3000;
let app = express()
app.use(express.json())
app.use(cookieParser())
app.use(cors({
    origin:"http://localhost:5173",
    credentials:true
}));
app.get('/', (req, res) => {
    res.send('server running ..!');
});
app.use("/api/auth", authRouter )
app.use("/api/user", userRouter )
app.use("/api/listing",listingRouter )
app.use("/api/booking",bookingRouter )
app.listen(port,()=>{
    connectDb();
    console.log("server started on port : " + port)
})