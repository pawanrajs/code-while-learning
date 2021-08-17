#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    # Remove 10% of elements
    how_many_to_remove = len(predictions) // 10
    
    residual_errors_list = [abs(p - n) for p, n in zip(predictions, net_worths)]
    all_errors_list = [(r, a, n) for r, a, n in zip(residual_errors_list, ages, net_worths)]

    for i in range(how_many_to_remove):
        all_errors_list.remove(max(all_errors_list))
    
    cleaned_data = [(a, n, r) for r, a, n in all_errors_list]

    return cleaned_data

