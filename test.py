import dogma
import sys
import mcb185

fl = sys.argv[1]
w = int(sys.argv[2])

def efficient_gc_skew(seq, window_size):
    total_length = len(seq)
    
    # Initial window
    current_window = seq[:window_size]
    skew_values = [gc_skew(current_window)]
    comp_values = [gc_comp(current_window)]

    # Move the window
    for i in range(window_size, total_length):
        # Drop one nucleotide on the left and add one on the right
        current_window = current_window[1:] + seq[i]

        # Calculate GC skew and composition for the current window
        skew_values.append(gc_skew(current_window))
        comp_values.append(gc_comp(current_window))

    return skew_values, comp_values

# Example usage with E.coli genome and 1000 nt windows
ecoli_genome = "ACGT..."  # Replace with the actual E.coli genome sequence
window_size = 1000

gc_skew_values, gc_comp_values = efficient_gc_skew(ecoli_genome, window_size)

# Now you can use gc_skew_values and gc_comp_values as needed
