import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();
const asyncGet = promisify(client.get).bind(client);

client.on('error', (err) => console.log('Redis Client Error: ', err.message));
client.on('connect', () => {
  console.log('Redis client connected to the server')
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const value = await asyncGet(schoolName);
  console.log(value);
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})()
