from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from queue import Queue, Empty

# job queue
q = Queue()

# /jobs
@api_view(['POST', 'GET', 'DELETE'])
def jobs(request):
    # add job
    if request.method == 'POST':
        job = request.data['input']
        if job not in q.queue:
            q.put(job, False)
            jobs = list(q.queue)
            jobs.reverse()
            return Response(jobs, status=status.HTTP_201_CREATED)
        # case where job already exists
        jobs = list(q.queue)
        jobs.reverse()
        return Response(jobs,status=status.HTTP_200_OK)
    # delete job
    elif request.method == 'DELETE':
        q.queue.clear()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # get all jobs
    elif request.method == 'GET':
        jobs = list(q.queue)
        jobs.reverse()
        return Response(jobs)


# /job => getjob
@api_view(['GET'])
def job(request):
    try:    
        job = q.get(False)
        return Response(job)
    except Empty:
        # case where queue is empty
        return Response(status=status.HTTP_204_NO_CONTENT)

        


