"""
Create the Page curve schematic diagram showing nested effective Hilbert spaces
This reproduces the conceptual figure showing how the effective Hilbert space shrinks over time
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Ellipse, FancyBboxPatch, Circle
import numpy as np

def create_page_curve_schematic(figsize=(8, 6), dpi=300):
    """
    Create schematic showing nested regions representing effective Hilbert space evolution
    """
    # Set up matplotlib for LaTeX rendering
    try:
        plt.rcParams.update({
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": ["Computer Modern Roman"],
            "mathtext.fontset": "cm",
            "axes.labelsize": 14,
            "font.size": 12,
        })
    except:
        plt.rcParams.update({
            "font.family": "serif",
            "axes.labelsize": 14,
            "font.size": 12,
        })
    
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    # Set up the plotting area
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Define nested ellipses (from outermost to innermost)
    # Representing ρ_sys(t) at different times
    
    # Outermost ellipse - entire system Hilbert space (background, hatched)
    outer_ellipse = Ellipse((0, 0), 6.5, 4.5, 
                           facecolor='lightgray', 
                           edgecolor='gray',
                           linewidth=2,
                           alpha=0.3,
                           hatch='///')
    ax.add_patch(outer_ellipse)
    
    # Second ellipse - effective Hilbert space at intermediate time
    mid_ellipse = Ellipse((0, 0), 4.8, 3.3, 
                         facecolor='gray', 
                         edgecolor='darkgray',
                         linewidth=2.5,
                         alpha=0.5)
    ax.add_patch(mid_ellipse)
    
    # Inner ellipse - effective Hilbert space at late time
    inner_ellipse = Ellipse((0, 0), 2.8, 1.9, 
                           facecolor='darkgray', 
                           edgecolor='black',
                           linewidth=2.5,
                           alpha=0.7)
    ax.add_patch(inner_ellipse)
    
    # Small innermost ellipse - black, representing final state
    final_ellipse = Ellipse((0.8, 0.1), 1.2, 0.7, 
                           facecolor='black', 
                           edgecolor='black',
                           linewidth=2)
    ax.add_patch(final_ellipse)
    
    # Add a white circle for the initial state label position
    initial_circle = Circle((-1.8, 0.5), 0.45, 
                          facecolor='white', 
                          edgecolor='blue',
                          linewidth=2.5,
                          zorder=10)
    ax.add_patch(initial_circle)
    
    # Add labels
    # Initial state
    ax.text(-1.8, 0.5, r'$|\Phi_{\rm sys}(0)\rangle$', 
            fontsize=11, ha='center', va='center',
            color='blue', weight='bold', zorder=11)
    
    # Final state region label
    ax.text(0.8, 0.1, r'$\mathcal{H}^{\rm eff}_{\rm S}(\infty)$', 
            fontsize=10, ha='center', va='center',
            color='white', weight='bold')
    
    # Arrow showing current evolution
    arrow_props = dict(arrowstyle='->', lw=3, color='red', 
                      connectionstyle="arc3,rad=0.1")
    ax.annotate('', xy=(0.2, 0.1), xytext=(-1.35, 0.5),
               arrowprops=arrow_props, zorder=12)
    
    # Label for ρ_sys at different times
    ax.text(-2.5, -1.7, r'$\rho_{\rm sys}(t_P)$', 
            fontsize=12, ha='center', va='center',
            style='italic')
    
    # Label for system Hilbert space
    ax.text(2.5, 1.5, r'$\mathcal{H}_{\rm sys}$', 
            fontsize=14, ha='center', va='center',
            weight='bold')
    
    # Add caption/description at the bottom
    caption_text = (
        r"FIG. 11.   Schematic picture of the dynamics leading to the\n"
        r"Page curve.  The full colored regions depict the size of the\n"
        r"effective Hilbert space that is necessary in order to represent\n"
        r"$\rho_{\rm sys}(t)$ at different times $t$. Darker colors correspond to later\n"
        r"times. In our case, where the particle current forces the\n"
        r"system $\mathcal{S}$ into a small effective Hilbert space $\mathcal{H}^{\rm eff}_{\rm S}(\infty)$. Al-\n"
        r"though the subspace $\dim \mathcal{H}^{\rm eff}_{\rm S}(\infty)$ is small, the environment at late times has\n"
        r"a complicated non-local structure, its von Neumann entropy\n"
        r"is bounded by $\ln \dim \mathcal{H}^{\rm eff}_{\rm S}(\infty)$. Similar scenarios could also\n"
        r"be realized in other models by forcing mechanisms like energy\n"
        r"or spin currents."
    )
    
    # Place caption below the figure
    fig.text(0.1, 0.02, caption_text, 
            fontsize=9, ha='left', va='bottom',
            wrap=True, family='serif')
    
    plt.tight_layout(rect=[0, 0.25, 1, 1])  # Leave space for caption
    
    return fig, ax


def create_simplified_page_curve_schematic(figsize=(8, 5), dpi=300):
    """
    Simplified version focusing on the nested structure without full caption
    """
    # Set up matplotlib for LaTeX rendering
    try:
        plt.rcParams.update({
            "text.usetex": True,
            "font.family": "serif",
            "font.serif": ["Computer Modern Roman"],
            "mathtext.fontset": "cm",
        })
    except:
        plt.rcParams.update({"font.family": "serif"})
    
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-2.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # Define colors from light to dark (representing time evolution)
    colors = ['#E8E8E8', '#C0C0C0', '#909090', '#404040']
    
    # Outermost - full system Hilbert space (hatched background)
    outer = Ellipse((0, 0), 6.5, 4.5, 
                   facecolor=colors[0], 
                   edgecolor='gray',
                   linewidth=2,
                   hatch='///',
                   alpha=0.4)
    ax.add_patch(outer)
    
    # Intermediate stages
    mid1 = Ellipse((0, 0), 4.8, 3.3, 
                  facecolor=colors[1], 
                  edgecolor='darkgray',
                  linewidth=2.5,
                  alpha=0.6)
    ax.add_patch(mid1)
    
    mid2 = Ellipse((0, 0), 2.8, 1.9, 
                  facecolor=colors[2], 
                  edgecolor='black',
                  linewidth=2.5,
                  alpha=0.8)
    ax.add_patch(mid2)
    
    # Final state (late time, small effective Hilbert space)
    final = Ellipse((0.8, 0.1), 1.2, 0.7, 
                   facecolor='black', 
                   edgecolor='black',
                   linewidth=2)
    ax.add_patch(final)
    
    # Initial state marker (white circle)
    initial = Circle((-1.8, 0.5), 0.45, 
                    facecolor='white', 
                    edgecolor='blue',
                    linewidth=2.5,
                    zorder=10)
    ax.add_patch(initial)
    
    # Labels
    ax.text(-1.8, 0.5, r'$|\Phi_{\rm sys}(0)\rangle$', 
            fontsize=12, ha='center', va='center',
            color='blue', weight='bold', zorder=11)
    
    ax.text(0.8, 0.1, r'$\mathcal{H}^{\rm eff}_{\rm S}(\infty)$', 
            fontsize=11, ha='center', va='center',
            color='white', weight='bold')
    
    # Evolution arrow
    arrow_props = dict(arrowstyle='->', lw=3.5, color='red')
    ax.annotate('', xy=(0.15, 0.15), xytext=(-1.3, 0.5),
               arrowprops=arrow_props, zorder=12)
    
    # Density matrix at Page time
    ax.text(-2.3, -1.6, r'$\rho_{\rm sys}(t_P)$', 
            fontsize=13, ha='center', va='center',
            style='italic')
    
    # Full system Hilbert space label
    ax.text(2.6, 1.6, r'$\mathcal{H}_{\rm sys}$', 
            fontsize=15, ha='center', va='center',
            weight='bold')
    
    plt.tight_layout()
    
    return fig, ax


if __name__ == "__main__":
    # Create the full version
    print("Creating Page curve schematic diagram...")
    fig1, ax1 = create_page_curve_schematic(dpi=300)
    fig1.savefig('page_curve_schematic_full.png', dpi=300, bbox_inches='tight')
    fig1.savefig('page_curve_schematic_full.pdf', bbox_inches='tight')
    print("Full version saved as page_curve_schematic_full.png/pdf")
    
    # Create simplified version
    fig2, ax2 = create_simplified_page_curve_schematic(dpi=300)
    fig2.savefig('page_curve_schematic_simple.png', dpi=300, bbox_inches='tight')
    fig2.savefig('page_curve_schematic_simple.pdf', bbox_inches='tight')
    print("Simplified version saved as page_curve_schematic_simple.png/pdf")
    
    plt.show()
