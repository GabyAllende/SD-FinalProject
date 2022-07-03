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
            var onoff = ["ON","OFF"]
            var bool = ["TRUE","FALSE"]
            var jsonFile = JSON.stringify(
                {   
                    control: onoff[getRandomIntInclusive(0,1)] ,
                    forward: bool[getRandomIntInclusive(0,1)],
                    ip: add.ip()
                }
            );
            console.log(JSON.parse(jsonFile))
            client.publish(process.env.TOPIC, jsonFile)
    
    },5000);
}


client.on('connect', ConnectEvent)


