let express=require('express');
let router=express.Router();

router.get("/employees",(req,res)=>{
    res.send("employees called");
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