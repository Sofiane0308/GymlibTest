from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from queue import Queue, Empty

# job queue
q = Queue()

def addJob(job):
    if job not in q.queue:
        q.put(job, False)
        return True
    return False

def clearQueue():
    q.queue.clear()

def getAllJobs():
    jobs = list(q.queue)
    jobs.reverse()
    return jobs

def popJob():
    return q.get(False)
    
    
    
    


# /jobs
@api_view(['POST', 'GET', 'DELETE'])
def jobs(request):
    # add job
    if request.method == 'POST':
        job = request.data['input']
        added = addJob(job)
        jobs = getAllJobs()
        if(added):
            #job added
            return Response(jobs, status=status.HTTP_201_CREATED)
        else:
            # case where job already exists
            return Response(jobs,status=status.HTTP_200_OK)

    # delete job
    elif request.method == 'DELETE':
        clearQueue()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # get all jobs
    elif request.method == 'GET':
        return Response(getAllJobs())


# /job => getjob
@api_view(['GET'])
def job(request):
    try:    
        return Response(popJob())
    except Empty:
        # case where queue is empty
        return Response(status=status.HTTP_204_NO_CONTENT)

        


