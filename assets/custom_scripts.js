<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <link rel="stylesheet" href="/assets/custom.css">
    <style>
        /* Inline CSS styles for custom animations */
        @keyframes bounceIn {
            from {
                opacity: 0;
                transform: scale(0.3);
            }
            50% {
                opacity: 1;
                transform: scale(1.1);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }
    </style>
</head>
<body>
    <div id="app"></div>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Adding hover effects to floating cards
            const cards = document.querySelectorAll('.floating-card');
            cards.forEach(card => {
                card.addEventListener('mouseover', () => {
                    card.style.transform = 'translateY(-5px)';
                    card.style.boxShadow = '0 8px 16px rgba(0, 0, 0, 0.3)';
                });
                card.addEventListener('mouseout', () => {
                    card.style.transform = 'translateY(0)';
                    card.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.3)';
                });
            });

            // Adding bounce-in animation to alerts
            const alertBox = document.querySelector('.alert-box');
            if (alertBox) {
                alertBox.style.animation = 'bounceIn 1s ease-in-out';
            }
        });
    </script>
</body>
</html>
