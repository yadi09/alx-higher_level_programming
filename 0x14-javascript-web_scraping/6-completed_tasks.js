#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('Error:', error)
  }

  const tasks = JSON.parse(body);

  const completedTasks = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!completedTasks[task.userId]) {
        completedTasks[task.userId] = 0;
      }
        completedTasks[task.userId]++;
    }
  });

  const result = Object.keys(completedTasks)
.filter(userId => completedTasks[userId] > 0)
.reduce((obj, userId) => {
    obj[userId] = completedTasks[userId];
    return obj;
}, {});

  console.log(result);
});
