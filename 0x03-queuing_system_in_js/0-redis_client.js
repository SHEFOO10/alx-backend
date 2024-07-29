import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis Client Error: ', err.message));
client.on('connect', () => console.log('Redis client connected to the server'));
