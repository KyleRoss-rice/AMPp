# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _DeepMimicCore
else:
    import _DeepMimicCore

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _DeepMimicCore.delete_SwigPyIterator

    def value(self):
        return _DeepMimicCore.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _DeepMimicCore.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _DeepMimicCore.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _DeepMimicCore.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _DeepMimicCore.SwigPyIterator_equal(self, x)

    def copy(self):
        return _DeepMimicCore.SwigPyIterator_copy(self)

    def next(self):
        return _DeepMimicCore.SwigPyIterator_next(self)

    def __next__(self):
        return _DeepMimicCore.SwigPyIterator___next__(self)

    def previous(self):
        return _DeepMimicCore.SwigPyIterator_previous(self)

    def advance(self, n):
        return _DeepMimicCore.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _DeepMimicCore.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _DeepMimicCore.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _DeepMimicCore.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _DeepMimicCore.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _DeepMimicCore.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _DeepMimicCore.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _DeepMimicCore:
_DeepMimicCore.SwigPyIterator_swigregister(SwigPyIterator)

class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _DeepMimicCore.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _DeepMimicCore.IntVector___nonzero__(self)

    def __bool__(self):
        return _DeepMimicCore.IntVector___bool__(self)

    def __len__(self):
        return _DeepMimicCore.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _DeepMimicCore.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _DeepMimicCore.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _DeepMimicCore.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _DeepMimicCore.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _DeepMimicCore.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _DeepMimicCore.IntVector___setitem__(self, *args)

    def pop(self):
        return _DeepMimicCore.IntVector_pop(self)

    def append(self, x):
        return _DeepMimicCore.IntVector_append(self, x)

    def empty(self):
        return _DeepMimicCore.IntVector_empty(self)

    def size(self):
        return _DeepMimicCore.IntVector_size(self)

    def swap(self, v):
        return _DeepMimicCore.IntVector_swap(self, v)

    def begin(self):
        return _DeepMimicCore.IntVector_begin(self)

    def end(self):
        return _DeepMimicCore.IntVector_end(self)

    def rbegin(self):
        return _DeepMimicCore.IntVector_rbegin(self)

    def rend(self):
        return _DeepMimicCore.IntVector_rend(self)

    def clear(self):
        return _DeepMimicCore.IntVector_clear(self)

    def get_allocator(self):
        return _DeepMimicCore.IntVector_get_allocator(self)

    def pop_back(self):
        return _DeepMimicCore.IntVector_pop_back(self)

    def erase(self, *args):
        return _DeepMimicCore.IntVector_erase(self, *args)

    def __init__(self, *args):
        _DeepMimicCore.IntVector_swiginit(self, _DeepMimicCore.new_IntVector(*args))

    def push_back(self, x):
        return _DeepMimicCore.IntVector_push_back(self, x)

    def front(self):
        return _DeepMimicCore.IntVector_front(self)

    def back(self):
        return _DeepMimicCore.IntVector_back(self)

    def assign(self, n, x):
        return _DeepMimicCore.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _DeepMimicCore.IntVector_resize(self, *args)

    def insert(self, *args):
        return _DeepMimicCore.IntVector_insert(self, *args)

    def reserve(self, n):
        return _DeepMimicCore.IntVector_reserve(self, n)

    def capacity(self):
        return _DeepMimicCore.IntVector_capacity(self)
    __swig_destroy__ = _DeepMimicCore.delete_IntVector

# Register IntVector in _DeepMimicCore:
_DeepMimicCore.IntVector_swigregister(IntVector)

class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _DeepMimicCore.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _DeepMimicCore.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _DeepMimicCore.DoubleVector___bool__(self)

    def __len__(self):
        return _DeepMimicCore.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _DeepMimicCore.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _DeepMimicCore.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _DeepMimicCore.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _DeepMimicCore.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _DeepMimicCore.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _DeepMimicCore.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _DeepMimicCore.DoubleVector_pop(self)

    def append(self, x):
        return _DeepMimicCore.DoubleVector_append(self, x)

    def empty(self):
        return _DeepMimicCore.DoubleVector_empty(self)

    def size(self):
        return _DeepMimicCore.DoubleVector_size(self)

    def swap(self, v):
        return _DeepMimicCore.DoubleVector_swap(self, v)

    def begin(self):
        return _DeepMimicCore.DoubleVector_begin(self)

    def end(self):
        return _DeepMimicCore.DoubleVector_end(self)

    def rbegin(self):
        return _DeepMimicCore.DoubleVector_rbegin(self)

    def rend(self):
        return _DeepMimicCore.DoubleVector_rend(self)

    def clear(self):
        return _DeepMimicCore.DoubleVector_clear(self)

    def get_allocator(self):
        return _DeepMimicCore.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _DeepMimicCore.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _DeepMimicCore.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _DeepMimicCore.DoubleVector_swiginit(self, _DeepMimicCore.new_DoubleVector(*args))

    def push_back(self, x):
        return _DeepMimicCore.DoubleVector_push_back(self, x)

    def front(self):
        return _DeepMimicCore.DoubleVector_front(self)

    def back(self):
        return _DeepMimicCore.DoubleVector_back(self)

    def assign(self, n, x):
        return _DeepMimicCore.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _DeepMimicCore.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _DeepMimicCore.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _DeepMimicCore.DoubleVector_reserve(self, n)

    def capacity(self):
        return _DeepMimicCore.DoubleVector_capacity(self)
    __swig_destroy__ = _DeepMimicCore.delete_DoubleVector

# Register DoubleVector in _DeepMimicCore:
_DeepMimicCore.DoubleVector_swigregister(DoubleVector)

class StringVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _DeepMimicCore.StringVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _DeepMimicCore.StringVector___nonzero__(self)

    def __bool__(self):
        return _DeepMimicCore.StringVector___bool__(self)

    def __len__(self):
        return _DeepMimicCore.StringVector___len__(self)

    def __getslice__(self, i, j):
        return _DeepMimicCore.StringVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _DeepMimicCore.StringVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _DeepMimicCore.StringVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _DeepMimicCore.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _DeepMimicCore.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _DeepMimicCore.StringVector___setitem__(self, *args)

    def pop(self):
        return _DeepMimicCore.StringVector_pop(self)

    def append(self, x):
        return _DeepMimicCore.StringVector_append(self, x)

    def empty(self):
        return _DeepMimicCore.StringVector_empty(self)

    def size(self):
        return _DeepMimicCore.StringVector_size(self)

    def swap(self, v):
        return _DeepMimicCore.StringVector_swap(self, v)

    def begin(self):
        return _DeepMimicCore.StringVector_begin(self)

    def end(self):
        return _DeepMimicCore.StringVector_end(self)

    def rbegin(self):
        return _DeepMimicCore.StringVector_rbegin(self)

    def rend(self):
        return _DeepMimicCore.StringVector_rend(self)

    def clear(self):
        return _DeepMimicCore.StringVector_clear(self)

    def get_allocator(self):
        return _DeepMimicCore.StringVector_get_allocator(self)

    def pop_back(self):
        return _DeepMimicCore.StringVector_pop_back(self)

    def erase(self, *args):
        return _DeepMimicCore.StringVector_erase(self, *args)

    def __init__(self, *args):
        _DeepMimicCore.StringVector_swiginit(self, _DeepMimicCore.new_StringVector(*args))

    def push_back(self, x):
        return _DeepMimicCore.StringVector_push_back(self, x)

    def front(self):
        return _DeepMimicCore.StringVector_front(self)

    def back(self):
        return _DeepMimicCore.StringVector_back(self)

    def assign(self, n, x):
        return _DeepMimicCore.StringVector_assign(self, n, x)

    def resize(self, *args):
        return _DeepMimicCore.StringVector_resize(self, *args)

    def insert(self, *args):
        return _DeepMimicCore.StringVector_insert(self, *args)

    def reserve(self, n):
        return _DeepMimicCore.StringVector_reserve(self, n)

    def capacity(self):
        return _DeepMimicCore.StringVector_capacity(self)
    __swig_destroy__ = _DeepMimicCore.delete_StringVector

# Register StringVector in _DeepMimicCore:
_DeepMimicCore.StringVector_swigregister(StringVector)

class ConstCharVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _DeepMimicCore.ConstCharVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _DeepMimicCore.ConstCharVector___nonzero__(self)

    def __bool__(self):
        return _DeepMimicCore.ConstCharVector___bool__(self)

    def __len__(self):
        return _DeepMimicCore.ConstCharVector___len__(self)

    def __getslice__(self, i, j):
        return _DeepMimicCore.ConstCharVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _DeepMimicCore.ConstCharVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _DeepMimicCore.ConstCharVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _DeepMimicCore.ConstCharVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _DeepMimicCore.ConstCharVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _DeepMimicCore.ConstCharVector___setitem__(self, *args)

    def pop(self):
        return _DeepMimicCore.ConstCharVector_pop(self)

    def append(self, x):
        return _DeepMimicCore.ConstCharVector_append(self, x)

    def empty(self):
        return _DeepMimicCore.ConstCharVector_empty(self)

    def size(self):
        return _DeepMimicCore.ConstCharVector_size(self)

    def swap(self, v):
        return _DeepMimicCore.ConstCharVector_swap(self, v)

    def begin(self):
        return _DeepMimicCore.ConstCharVector_begin(self)

    def end(self):
        return _DeepMimicCore.ConstCharVector_end(self)

    def rbegin(self):
        return _DeepMimicCore.ConstCharVector_rbegin(self)

    def rend(self):
        return _DeepMimicCore.ConstCharVector_rend(self)

    def clear(self):
        return _DeepMimicCore.ConstCharVector_clear(self)

    def get_allocator(self):
        return _DeepMimicCore.ConstCharVector_get_allocator(self)

    def pop_back(self):
        return _DeepMimicCore.ConstCharVector_pop_back(self)

    def erase(self, *args):
        return _DeepMimicCore.ConstCharVector_erase(self, *args)

    def __init__(self, *args):
        _DeepMimicCore.ConstCharVector_swiginit(self, _DeepMimicCore.new_ConstCharVector(*args))

    def push_back(self, x):
        return _DeepMimicCore.ConstCharVector_push_back(self, x)

    def front(self):
        return _DeepMimicCore.ConstCharVector_front(self)

    def back(self):
        return _DeepMimicCore.ConstCharVector_back(self)

    def assign(self, n, x):
        return _DeepMimicCore.ConstCharVector_assign(self, n, x)

    def resize(self, *args):
        return _DeepMimicCore.ConstCharVector_resize(self, *args)

    def insert(self, *args):
        return _DeepMimicCore.ConstCharVector_insert(self, *args)

    def reserve(self, n):
        return _DeepMimicCore.ConstCharVector_reserve(self, n)

    def capacity(self):
        return _DeepMimicCore.ConstCharVector_capacity(self)
    __swig_destroy__ = _DeepMimicCore.delete_ConstCharVector

# Register ConstCharVector in _DeepMimicCore:
_DeepMimicCore.ConstCharVector_swigregister(ConstCharVector)

class cDeepMimicCore(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, enable_draw):
        _DeepMimicCore.cDeepMimicCore_swiginit(self, _DeepMimicCore.new_cDeepMimicCore(enable_draw))
    __swig_destroy__ = _DeepMimicCore.delete_cDeepMimicCore

    def SeedRand(self, seed):
        return _DeepMimicCore.cDeepMimicCore_SeedRand(self, seed)

    def ParseArgs(self, args):
        return _DeepMimicCore.cDeepMimicCore_ParseArgs(self, args)

    def Init(self):
        return _DeepMimicCore.cDeepMimicCore_Init(self)

    def Update(self, timestep):
        return _DeepMimicCore.cDeepMimicCore_Update(self, timestep)

    def Reset(self):
        return _DeepMimicCore.cDeepMimicCore_Reset(self)

    def GetTime(self):
        return _DeepMimicCore.cDeepMimicCore_GetTime(self)

    def GetName(self):
        return _DeepMimicCore.cDeepMimicCore_GetName(self)

    def EnableDraw(self):
        return _DeepMimicCore.cDeepMimicCore_EnableDraw(self)

    def Draw(self):
        return _DeepMimicCore.cDeepMimicCore_Draw(self)

    def Keyboard(self, key, x, y):
        return _DeepMimicCore.cDeepMimicCore_Keyboard(self, key, x, y)

    def MouseClick(self, button, state, x, y):
        return _DeepMimicCore.cDeepMimicCore_MouseClick(self, button, state, x, y)

    def MouseMove(self, x, y):
        return _DeepMimicCore.cDeepMimicCore_MouseMove(self, x, y)

    def Reshape(self, w, h):
        return _DeepMimicCore.cDeepMimicCore_Reshape(self, w, h)

    def Shutdown(self):
        return _DeepMimicCore.cDeepMimicCore_Shutdown(self)

    def IsDone(self):
        return _DeepMimicCore.cDeepMimicCore_IsDone(self)

    def GetDrawScene(self):
        return _DeepMimicCore.cDeepMimicCore_GetDrawScene(self)

    def SetPlaybackSpeed(self, speed):
        return _DeepMimicCore.cDeepMimicCore_SetPlaybackSpeed(self, speed)

    def SetUpdatesPerSec(self, updates_per_sec):
        return _DeepMimicCore.cDeepMimicCore_SetUpdatesPerSec(self, updates_per_sec)

    def GetWinWidth(self):
        return _DeepMimicCore.cDeepMimicCore_GetWinWidth(self)

    def GetWinHeight(self):
        return _DeepMimicCore.cDeepMimicCore_GetWinHeight(self)

    def GetNumUpdateSubsteps(self):
        return _DeepMimicCore.cDeepMimicCore_GetNumUpdateSubsteps(self)

    def IsRLScene(self):
        return _DeepMimicCore.cDeepMimicCore_IsRLScene(self)

    def GetNumAgents(self):
        return _DeepMimicCore.cDeepMimicCore_GetNumAgents(self)

    def NeedNewAction(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_NeedNewAction(self, agent_id)

    def RecordState(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_RecordState(self, agent_id)

    def RecordGoal(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_RecordGoal(self, agent_id)

    def SetAction(self, agent_id, action):
        return _DeepMimicCore.cDeepMimicCore_SetAction(self, agent_id, action)

    def LogVal(self, agent_id, val):
        return _DeepMimicCore.cDeepMimicCore_LogVal(self, agent_id, val)

    def GetActionSpace(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetActionSpace(self, agent_id)

    def GetStateSize(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetStateSize(self, agent_id)

    def GetGoalSize(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetGoalSize(self, agent_id)

    def GetActionSize(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetActionSize(self, agent_id)

    def GetNumActions(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetNumActions(self, agent_id)

    def BuildStateOffset(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildStateOffset(self, agent_id)

    def BuildStateScale(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildStateScale(self, agent_id)

    def BuildGoalOffset(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildGoalOffset(self, agent_id)

    def BuildGoalScale(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildGoalScale(self, agent_id)

    def BuildActionOffset(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildActionOffset(self, agent_id)

    def BuildActionScale(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildActionScale(self, agent_id)

    def BuildActionBoundMin(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildActionBoundMin(self, agent_id)

    def BuildActionBoundMax(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildActionBoundMax(self, agent_id)

    def BuildStateNormGroups(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildStateNormGroups(self, agent_id)

    def BuildGoalNormGroups(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_BuildGoalNormGroups(self, agent_id)

    def CalcReward(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_CalcReward(self, agent_id)

    def GetRewardMin(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetRewardMin(self, agent_id)

    def GetRewardMax(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetRewardMax(self, agent_id)

    def GetRewardFail(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetRewardFail(self, agent_id)

    def GetRewardSucc(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_GetRewardSucc(self, agent_id)

    def EnableAMPTaskReward(self):
        return _DeepMimicCore.cDeepMimicCore_EnableAMPTaskReward(self)

    def GetAMPObsSize(self):
        return _DeepMimicCore.cDeepMimicCore_GetAMPObsSize(self)

    def GetAMPObsOffset(self):
        return _DeepMimicCore.cDeepMimicCore_GetAMPObsOffset(self)

    def GetAMPObsScale(self):
        return _DeepMimicCore.cDeepMimicCore_GetAMPObsScale(self)

    def GetAMPObsNormGroup(self):
        return _DeepMimicCore.cDeepMimicCore_GetAMPObsNormGroup(self)

    def RecordAMPObsAgent(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_RecordAMPObsAgent(self, agent_id)

    def RecordAMPObsExpert(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_RecordAMPObsExpert(self, agent_id)

    def IsEpisodeEnd(self):
        return _DeepMimicCore.cDeepMimicCore_IsEpisodeEnd(self)

    def CheckValidEpisode(self):
        return _DeepMimicCore.cDeepMimicCore_CheckValidEpisode(self)

    def CheckTerminate(self, agent_id):
        return _DeepMimicCore.cDeepMimicCore_CheckTerminate(self, agent_id)

    def SetMode(self, mode):
        return _DeepMimicCore.cDeepMimicCore_SetMode(self, mode)

    def SetSampleCount(self, count):
        return _DeepMimicCore.cDeepMimicCore_SetSampleCount(self, count)

# Register cDeepMimicCore in _DeepMimicCore:
_DeepMimicCore.cDeepMimicCore_swigregister(cDeepMimicCore)



