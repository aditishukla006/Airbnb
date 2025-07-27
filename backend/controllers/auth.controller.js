import genToken from "../config/token.js"
import User from "../model/user.model.js"
import bcrypt from "bcryptjs"

export const sighUp=async (req,res) => {
    try {
        let {name,email,password} = req.body
        let existUser = await User.findOne({email})
        if(existUser){
            return res.status(400).json({message:"User is already exist"})
        }
        let hashPassword = await bcrypt.hash(password,10)
        let user = await User.create({name , email , password:hashPassword})
        let token = await genToken(user._id)
        res.cookie("token",token,{
            httpOnly:true,
            secure:process.env.NODE_ENVIRONMENT = "production",
            sameSite: "strict",
            maxAge: 7 * 24 * 60 * 60 * 1000


        })
        return res.status(201).json(user)

    } catch (error) {
        return res.status(500).json({message:`sighup error ${error}`})
    }
    
}
export const login = async (req,res) => {
    try {
        let {email,password} = req.body
        let user= await User.findOne({email}).populate("listing","title image1 image2 image3 description rent category city landMark")
        if(!user){
            return res.status(400).json({message:"User is not exist"})
        }
        let isMatch = await bcrypt.compare(password,user.password)
        if(!isMatch){
            return res.status(400).json({message:"incorrect Password"})
        }
        let token = await genToken(user._id)
        res.cookie("token",token,{
            httpOnly:true,
            secure:process.env.NODE_ENVIRONMENT = "production",
            sameSite: "strict",
            maxAge: 7 * 24 * 60 * 60 * 1000


        })
        return res.status(200).json(user)
        
    } catch (error) {
        return res.status(500).json({message:`login error ${error}`})
    }
    
}
export const logOut = async (req,res) => {
    try {
        res.clearCookie("token")
        return res.status(200).json({message:"Logout Successfully"})
    } catch (error) {
        return res.status(500).json({message:`logout error ${error}`})
    }
}