const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const obj of jobs) {
    const job = queue.create('push_notification_code_3', obj);
  
    job
      .on('enqueue', () => console.log('Notification job created:', job.id))
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed:`, err);
      })
      .on('progress', (progress, _data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
