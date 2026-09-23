let express=require('express');
let router=express.Router();
let users=require('../models/users');

router.get("/employees",async(req,res)=>{
    let result=await users.find();
    res.send(result);
});

router.post("/assign-task",(req,res)=>{
    res.send("assign task page called");
})

router.get("/tasks",(req,res)=>{
    res.send("tasks page called");
});

router.get("/notifications",(req,res)=>{
    res.send("notifications page called");
})
module.exports=router;