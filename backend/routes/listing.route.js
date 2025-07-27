import express from "express"
import isAuth from "../middleware/isAuth.js"
import upload from "../middleware/multer.js"
import { addListing, deleteListing, findListing, getListing, ratingListing, search, updateListing } from "../controllers/listing.controller.js"

let listingRouter = express.Router()


listingRouter.post("/add",isAuth,upload.fields([
    {name:"image1",maxCount:1},
    {name:"image2",maxCount:1},
    {name:"image3",maxCount:1}
]),addListing)

listingRouter.get("/get",getListing)
listingRouter.get("/findlistingbyid/:id",isAuth,findListing)
listingRouter.delete("/delete/:id",isAuth,deleteListing)
listingRouter.post("/ratings/:id",isAuth,ratingListing)
listingRouter.get("/search",search)

listingRouter.post("/update/:id",isAuth,upload.fields([
    {name:"image1",maxCount:1},
    {name:"image2",maxCount:1},
    {name:"image3",maxCount:1}
]),updateListing)

export default listingRouter