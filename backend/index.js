import express from "express"
import dotenv from "dotenv"
import connectDb from "./config/db.js"
import authRouter from "./routes/auth.route.js"
import cookieParser from "cookie-parser"
import cors from "cors"
import userRouter from "./routes/user.route.js"
import listingRouter from "./routes/listing.route.js"
import bookingRouter from "./routes/booking.route.js"

dotenv.config()

const app = express()
const port = process.env.PORT || 3000

app.use(express.json())
app.use(cookieParser())

app.use(cors({
    origin: function(origin, callback){
        // allow requests with no origin (like Postman)
        if(!origin) return callback(null, true); 
        const allowedOrigins = [
            "http://localhost:5173",
            "https://airbnb-git-main-aditishukla006s-projects.vercel.app"
        ];
        if(allowedOrigins.includes(origin)) {
            callback(null, true);
        } else {
            callback(new Error("CORS not allowed for this origin"), false);
        }
    },
    credentials: true
}));


app.get('/', (req, res) => {
    res.send('server running ..!');
});

app.use("/api/auth", authRouter)
app.use("/api/user", userRouter)
app.use("/api/listing", listingRouter)
app.use("/api/booking", bookingRouter)

app.listen(port, () => {
    connectDb()
    console.log("server started on port : " + port)
})
