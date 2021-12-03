import simpy
import random
import numpy as np

class System(object):
    # TODO: priority queue
    def __init__(self, env, server_count, service_time_distribution, sptf = False):
        self.env = env
        self.sptf = sptf
        if not sptf:
            self.servers = simpy.Resource(self.env, server_count)
        else:
            self.servers = simpy.resources.resource.PriorityResource(self.env, server_count)
        self.service_time = service_time_distribution
        self.ts_arrival = []
        self.ts_sojourn = []
        self.ts_service = []
        self.ts_waiting = []
#         self.Ns = []
        self.N = 0
    
    def serve(self, customer, service_time):
        """ Offers service to one customer"""
        yield self.env.timeout(service_time)

    def request_service(self, customer):
        """Request service"""
        service_time = self.service_time()
        arrival_time = self.env.now
        kwargs = {}
        if self.sptf:
            kwargs["priority"] = service_time
            kwargs["preempt"] = False

        with self.servers.request(**kwargs) as request:
            self.N +=1
            yield request
            service_start_time = self.env.now
            self.ts_arrival.append(arrival_time)
            self.ts_waiting.append(service_start_time - arrival_time)
            self.ts_service.append(service_time)
            yield self.env.process(self.serve(customer, service_time))
        self.N -= 1
        self.ts_sojourn.append(self.env.now - arrival_time)
    
def sim_setup(system, interarrival_t_distribution):
    customer_id = 0
    while True:
        arrive_t = interarrival_t_distribution()
        yield system.env.timeout(arrive_t)
        customer_id += 1
        system.env.process(system.request_service(customer_id))
