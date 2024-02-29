#include <QApplication> // Include the QApplication header
#include <QMainWindow> // Include the QMainWindow header
#include <QLabel> // Include the QLabel header
#include <QPushButton> // Include the QPushButton header
#include <QClipboard> // Include the QClipboard header
#include <QMessageBox> // Include the QMessageBox header
#include <QTimer> // Include the QTimer header
#include <QMouseEvent> // Include the QMouseEvent header
#include <QColor> // Include the QColor header
#include <QDebug> // Include the qDebug header

class HexGrabber : public QMainWindow { // Define a class HexGrabber that inherits from QMainWindow
    Q_OBJECT // Macro required for signals and slots

public:
    HexGrabber(QWidget *parent = nullptr) : QMainWindow(parent) { // Constructor for the HexGrabber class
        setWindowTitle("Hex Grabber"); // Set the window title
        setFixedSize(400, 300); // Set the fixed size of the window

        // Label to display the color value
        colorLabel = new QLabel("Color at pointer: N/A", this); // Create a new QLabel
        colorLabel->setGeometry(50, 50, 300, 30); // Set the geometry of the label

        // Button to copy color value to clipboard
        copyButton = new QPushButton("Copy to Clipboard", this); // Create a new QPushButton
        copyButton->setGeometry(50, 100, 150, 30); // Set the geometry of the button
        connect(copyButton, &QPushButton::clicked, this, &HexGrabber::copyToClipboard); // Connect button click signal to slot
    }

protected:
    void mousePressEvent(QMouseEvent *event) override { // Override mousePressEvent function
        if (event->button() == Qt::RightButton) { // Check if right mouse button is pressed
            updateColorValue(); // Call function to update color value
        }
    }

    void keyPressEvent(QKeyEvent *event) override { // Override keyPressEvent function
        if (event->key() == Qt::Key_R) { // Check if "R" key is pressed
            resetBackgroundColor(); // Call function to reset background color
        }
    }

private slots:
    void updateColorValue() { // Slot function to update color value
        QPoint cursorPos = QCursor::pos(); // Get cursor position
        QColor pixelColor = QColor::fromRgb(QGuiApplication::primaryScreen()->grabWindow(0, cursorPos.x(), cursorPos.y(), 1, 1).toImage().pixel(0, 0)); // Get color at cursor position
        QString hexValue = pixelColor.name(); // Get color value in hexadecimal format
        colorLabel->setText("Color at pointer: " + hexValue); // Update label text with color value
        setStyleSheet(QString("background-color: %1;").arg(hexValue)); // Set background color of window
    }

    void resetBackgroundColor() { // Slot function to reset background color
        setStyleSheet(""); // Clear the style sheet to reset background color
    }

    void copyToClipboard() { // Slot function to copy color value to clipboard
        QString hexValue = colorLabel->text().split(": ").last(); // Get color value from label
        QClipboard *clipboard = QApplication::clipboard(); // Get clipboard
        clipboard->setText(hexValue); // Set clipboard text to color value
        QMessageBox::information(this, "Copied to Clipboard", "Color value copied to clipboard!"); // Show message box
    }

private:
    QLabel *colorLabel; // Pointer to QLabel for displaying color value
    QPushButton *copyButton; // Pointer to QPushButton for copying color value to clipboard
    QTimer *timer; // Pointer to QTimer for updating color value periodically
};

int main(int argc, char *argv[]) { // Main function
    QApplication app(argc, argv); // Create the QApplication object
    HexGrabber hexGrabber; // Create an instance of the HexGrabber class
    hexGrabber.show(); // Show the main window
    return app.exec(); // Enter the application event loop
}

#include "main.moc" // Include the meta object compiler generated file
