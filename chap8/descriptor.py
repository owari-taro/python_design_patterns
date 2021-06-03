from typing import ValuesView


class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name: str):
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, owner, name):
        print("_set_name is being called")
        self._name = name

    def __set__(self, instance, value):
        self._track_change_in_value_for(instance, value)
        instance.__dict__[self._name] = value

    def __get__(self, instance, owner):
        print("__get is being called")
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def _track_change_in_value_for(self, instance, value):
        self._set_default(instance)
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(ValuesView)

    def _needs_to_track_change(self, instance, value) -> bool:
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True
        return value != current_value

    def _set_default(self, instance):
        instance.__dict__.setdefault(self.trace_attribute_name, [])


class Traveler:
    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name: str, current_city: str):
        self.name = name
        self.current_city = current_city
