import mongoose from "mongoose";


const listingSchema = new mongoose.Schema({
    title:{
        type:String,
        required:true
    },
    description:{
        type:String,
        required:true
    },
    host:{
        type:mongoose.Schema.Types.ObjectId,
        ref:"User",
        required:true
    },
    guest:{
        type:mongoose.Schema.Types.ObjectId,
        ref:"User"
        
    },
    image1:{
        type:String,
        required:true
    },
    image2:{
        type:String,
        required:true
    },
    image3:{
        type:String,
        required:true
    },
    rent:{
        type:Number,
        required:true
    },
    city:{
        type:String,
        require:true

    },
    landMark:{
        type:String,
        require:true

    },
    category:{
        type:String,
        require:true

    },
    ratings:{
        type:Number,
        min:0,
        max:5,
        default:0
    },
    isBooked:{
        type:Boolean,
        default:false
    }


},{timestamps:true})

const Listing = mongoose.model( "Listing" , listingSchema)

export default Listing
