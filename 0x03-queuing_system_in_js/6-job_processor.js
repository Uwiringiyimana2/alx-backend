import { createQueue } from 'kue';

const queue = createQueue();

queue.process('push_notification_code', (job) => {
  sendNotification(job.data.phoneNumber, job.data.message);
});

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};
