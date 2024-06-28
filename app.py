from flask import Flask
from flask_cors import CORS

# Import your blueprints
from controller.UserMasterServlet import user_master_blueprint
from controller.AddressMasterServlet import address_master_blueprint
from controller.ImageMasterServlet import image_master_blueprint
from controller.OrderDetailsServlet import order_details_blueprint
from controller.OrderMasterServlet import order_master_blueprint
from controller.ProductDetailsServlet import product_details_blueprint
from controller.ProductMasterServlet import product_master_blueprint
from controller.VendorMasterServlet import vendor_master_blueprint

app = Flask(__name__)

# Initialize CORS for any origin
CORS(app, origins=["*"]) # Replace with your mobile's IP and port

# Register blueprints
app.register_blueprint(user_master_blueprint)
app.register_blueprint(address_master_blueprint)
app.register_blueprint(image_master_blueprint)
app.register_blueprint(order_details_blueprint)
app.register_blueprint(order_master_blueprint)
app.register_blueprint(product_details_blueprint)
app.register_blueprint(product_master_blueprint)
app.register_blueprint(vendor_master_blueprint)

print("Flask app running on host:", app.config['SERVER_NAME'])

# Run the app in debug mode for development (remove in production)
if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
