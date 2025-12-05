/*import { v2 as cloudinary } from 'cloudinary';
import fs from "fs"

const uploadOnCloudinary = async (filepath) => {
    cloudinary.config({ 
        cloud_name: process.env.CLOUDINARY_CLOUD_NAME, 
        api_key: process.env.CLOUDINARY_API_KEY, 
        api_secret: process.env.CLOUDINARY_API_SECRET
    });
    try {
        if(!filepath){
            return null}
        const uploadResult = await cloudinary.uploader
        .upload(filepath)
        fs.unlinkSync(filepath)
        return uploadResult.secure_url


        
    } catch (error) {
        fs.unlinkSync(filepath)
        console.log(error)
    }
}

export default uploadOnCloudinary
    
*/
import { v2 as cloudinary } from 'cloudinary';
import fs from "fs"

const uploadOnCloudinary = async (filepath) => {
    cloudinary.config({ 
        cloud_name: process.env.CLOUDINARY_CLOUD_NAME, 
        api_key: process.env.CLOUDINARY_API_KEY, 
        api_secret: process.env.CLOUDINARY_API_SECRET
    });

    try {
        if (!filepath) return null;

        const uploadResult = await cloudinary.uploader.upload(filepath);

        // Safe unlink
        if (fs.existsSync(filepath)) {
            fs.unlinkSync(filepath);
        }

        return uploadResult.secure_url;

    } catch (error) {

        // Safe unlink even on failure
        if (fs.existsSync(filepath)) {
            fs.unlinkSync(filepath);
        }

        console.log("Cloudinary error:", error);
        return null;
    }
};

export default uploadOnCloudinary;
