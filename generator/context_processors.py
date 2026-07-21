from .models import Pair

def pair_processor(request):
    if request.user.is_authenticated:
        pair = Pair.get_pair_for_user(request.user)
    else:
        pair = None
    return {'pair': pair}