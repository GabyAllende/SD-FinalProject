const mqtt = require('mqtt')
const client  = mqtt.connect('mqtt://'+process.env.HOST+':'+process.env.PORT)
 
const moment = require('moment');
const os = require('os');
const add = require('address');

function getRandomIntInclusive(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min);
  }
  
function ConnectEvent(){
    setInterval(
        function(){
            
            var jsonFile = JSON.stringify(
                {   
                    ID: "xxx" ,
                    Owner: "Allende"
                }
            );
            console.log(JSON.parse(jsonFile))
            client.publish(process.env.TOPIC, jsonFile)
    
    },3000);
}


client.on('connect', ConnectEvent)


