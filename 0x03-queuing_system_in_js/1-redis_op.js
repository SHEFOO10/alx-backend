import redis from 'redis';

const client = redis.createClient();
let clientReady = false;

client.on('error', (err) => console.log('Redis Client Error: ', err.message));
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => console.log(value));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
