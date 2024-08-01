function createPushNotificationsJobs(jobs, queue) {
    if (!Array.isArray(jobs))
        throw new Error('Jobs is not an array');
    jobs.forEach((jobData) => {
        const job = queue.create('push_notification_code_3', jobData);
        job.save((err) => {
            console.log(job.id);
            if (!err) console.log(`Notification job created: ${job.id}`);
        });
        console.log(job)
        job.on('complete', () => console.log(`Notification job ${job.id} completed`));
        job.on('failed', (errorMessage) => console.log(`Notification job ${job.id} failed: ${errorMessage}`));
        job.on('progress', (progress) => console.log(`Notification job ${job.id} ${progress}% complete`));
    });
}

export default createPushNotificationsJobs;