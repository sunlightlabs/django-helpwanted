from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list_detail import object_list, object_detail
from helpwanted.models import JobListing, POSITION_TYPE_CHOICES

def joblisting_list(request, page=1):
    jobs = JobListing.objects.open()
    return object_list(request, queryset=jobs, paginate_by=10, template_object_name="job")

def joblisting_detail(request, object_id):
    jobs = JobListing.objects.filter(pk=object_id)
    other_jobs = JobListing.objects.open().exclude(pk=object_id).order_by("?")[:5]
    try:
        return object_detail(request, queryset=jobs, object_id=object_id, template_object_name="job", extra_context={"other_jobs":other_jobs})
    except Http404:
        return HttpResponseRedirect(reverse('job_list'))
    