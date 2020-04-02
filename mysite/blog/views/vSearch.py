from django.shortcuts import render
from django.contrib.postgres.search import (
    SearchVector,  SearchQuery, SearchRank, TrigramSimilarity)
from blog.models import Post
from blog.forms import SearchForm


def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(search=search_vector, rank=SearchRank(
                search_vector, search_query))\
                .filter(search=search_query).order_by('-rank')
    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})


"""NOTE_START 
# ---Group Building a search view
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.annotate(
                search=SearchVector('title', 'body'))\
                .filter(search=query)
    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})
NOTE_END"""

"""NOTE_START 
# ---Group Stemming and ranking results
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(search=search_vector, rank=SearchRank(
                search_vector, search_query))\
                .filter(search=search_query).order_by('-rank')
    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})
NOTE_END"""

"""NOTE_START 
# ---Group Weighting queries
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_vector =\
                SearchVector('title', weight='A') + \
                SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')
    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})
NOTE_END""" 

"""NOTE_START  
# ---Group TrigramSimilarity
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', 'body')
            search_vector =\
                SearchVector('title', weight='A') + \
                SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')
    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})
NOTE_END"""