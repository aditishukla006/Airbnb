import express from "express"
import isAuth from "../middleware/isAuth.js"
import { getCurrentUser } from "../controllers/user.controller.js"


let userRouter = express.Router()

userRouter.get("/currentuser",isAuth,getCurrentUser)

export default userRouter

