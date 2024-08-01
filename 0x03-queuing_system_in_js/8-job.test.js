import kue from 'kue';
import createPushNotificationsJobs from './8-job';
import { expect } from 'chai';
import sinon from 'sinon';

const jobs = [
    {
        phoneNumber: '4153518795',
        message: 'This is the code 1244 to verify your account'
    },
    {
        phoneNumber: '4153518790',
        message: 'This is the code 2943 to verify your account'
    }
];

const queue = kue.createQueue();

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

describe('createPushNotificationsJobs', () => {
    it('should create two jobs to the queue', () => {
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
    });
    it('should return an error when jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('jobs', queue)).to.throw(Error, 'Jobs is not an array');
    });
    it('should console log Notification job created: ${job.id}', () => {
        const consoleSpy = sinon.spy(console, 'log');
        createPushNotificationsJobs(jobs, queue);
        expect(consoleSpy.calledTwice).to.be.true;
        expect(consoleSpy.calledWith(sinon.match(/^Notification job created: [0-9]+$/))).to.be.true;
        consoleSpy.restore();
    });
    it('should console log Notification job ${job.id} completed', () => {
        const consoleSpy = sinon.spy(console, 'log');
        createPushNotificationsJobs(jobs, queue);
        queue.testMode.jobs.forEach((job) => job.emit('complete'));
        expect(consoleSpy.callCount).to.equal(4);
        expect(consoleSpy.calledWith(sinon.match(/^Notification job [0-9]+ completed$/))).to.be.true;
        consoleSpy.restore();
    });
    it('should console log Notification job ${job.id} failed: ${errorMessage}', () => {
        const consoleSpy = sinon.spy(console, 'log');
        createPushNotificationsJobs(jobs, queue);
        queue.testMode.jobs.forEach((job) => job.emit('failed', 'error message'));
        expect(consoleSpy.callCount).to.equal(4);
        expect(consoleSpy.calledWith(sinon.match(/^Notification job [0-9]+ failed: error message$/))).to.be.true;
        consoleSpy.restore();
    });
});
