import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const job = queue.create('push_notification_code', {
  phoneNumber: '0783481016',
  message: 'This is the code to verify your account',
});

job
  .on('enqueue', () => {
    console.log('Notification job created', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempts', () => {
    console.log('Notification job failed');
  });
job.save();
