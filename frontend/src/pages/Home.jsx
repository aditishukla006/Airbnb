import React, { useContext } from 'react'
import Nav from '../Component/Nav'


import Card from '../Component/Card';
import { listingDataContext } from '../Context/ListingContext';



function Home() {
  let {listingData,setListingData,newListData}=useContext(listingDataContext)
  
  return (
    <div>
     <Nav/>
     <div className='w-[100vw]  flex items-center justify-center gap-[25px] flex-wrap mt-[250px] md:mt-[180px]'>
     {newListData.map((list)=>(
      <Card title={list.title} landMark={list.landMark} city={list.city} image1={list.image1} image2={list.image2} image3={list.image3} rent={list.rent} id={list._id} ratings={list.ratings} isBooked={list.isBooked} host={list.host}/>
     ))}
     </div>
      </div> 
  )
}

export default Home
