from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AirportRouteForm
from .models import AirportRoute
from .utils import find_nth_node




def add_airport_route(request):
    if request.method == "POST":
        form = AirportRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_airport_route")
    else:
        form = AirportRouteForm()

    return render(request, "flightapp/add_route.html", {"form": form})


def nth_node_search(request):
    result = None

    if request.method == "POST":
        root_id = request.POST.get("root")
        direction = request.POST.get("direction")  # 'L' or 'R'
        n = int(request.POST.get("n"))

        root = AirportRoute.objects.get(id=root_id)
        result = find_nth_node(root, direction, n)

    roots = AirportRoute.objects.filter(parent__isnull=True)

    return render(
        request,
        "flightapp/nth_search.html",
        {"roots": roots, "result": result}
    )


def longest_node(request):
    node = AirportRoute.objects.order_by("-duration").first()
    return render(request, "flightapp/longest.html", {"node": node})


def shortest_between_two(request):
    result = None
    airports = AirportRoute.objects.all()

    if request.method == "POST":
        a1_id = request.POST.get("a1")
        a2_id = request.POST.get("a2")

        a1 = AirportRoute.objects.get(id=a1_id)
        a2 = AirportRoute.objects.get(id=a2_id)

        low = min(a1.duration, a2.duration)
        high = max(a1.duration, a2.duration)

        result = (
            AirportRoute.objects
            .filter(duration__gte=low, duration__lte=high)
            .order_by("duration")
            .first()
        )

    return render(
        request,
        "flightapp/shortest.html",
        {"airports": airports, "result": result}
    )
