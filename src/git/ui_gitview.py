# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gitview.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_GitWidget(object):
    def setupUi(self, GitWidget):
        if not GitWidget.objectName():
            GitWidget.setObjectName(u"GitWidget")
        GitWidget.resize(400, 300)
        self.verticalLayout = QVBoxLayout(GitWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.source_layout = QHBoxLayout()
        self.source_layout.setObjectName(u"source_layout")
        self.source_label = QLabel(GitWidget)
        self.source_label.setObjectName(u"source_label")

        self.source_layout.addWidget(self.source_label)

        self.source_cbx = QComboBox(GitWidget)
        self.source_cbx.setObjectName(u"source_cbx")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_cbx.sizePolicy().hasHeightForWidth())
        self.source_cbx.setSizePolicy(sizePolicy)
        self.source_cbx.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.source_layout.addWidget(self.source_cbx)


        self.verticalLayout.addLayout(self.source_layout)

        self.destinations_layout = QVBoxLayout()
        self.destinations_layout.setObjectName(u"destinations_layout")
        self.destinations_label = QLabel(GitWidget)
        self.destinations_label.setObjectName(u"destinations_label")

        self.destinations_layout.addWidget(self.destinations_label)

        self.destinations_table = QTableView(GitWidget)
        self.destinations_table.setObjectName(u"destinations_table")

        self.destinations_layout.addWidget(self.destinations_table)


        self.verticalLayout.addLayout(self.destinations_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.merge_button = QPushButton(GitWidget)
        self.merge_button.setObjectName(u"merge_button")

        self.horizontalLayout.addWidget(self.merge_button)

        self.push_button = QPushButton(GitWidget)
        self.push_button.setObjectName(u"push_button")

        self.horizontalLayout.addWidget(self.push_button)

        self.push_merger_button = QPushButton(GitWidget)
        self.push_merger_button.setObjectName(u"push_merger_button")

        self.horizontalLayout.addWidget(self.push_merger_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(GitWidget)

        QMetaObject.connectSlotsByName(GitWidget)
    # setupUi

    def retranslateUi(self, GitWidget):
        GitWidget.setWindowTitle(QCoreApplication.translate("GitWidget", u"Form", None))
        self.source_label.setText(QCoreApplication.translate("GitWidget", u"Source:", None))
        self.destinations_label.setText(QCoreApplication.translate("GitWidget", u"Destinations:", None))
        self.merge_button.setText(QCoreApplication.translate("GitWidget", u"Merge", None))
        self.push_button.setText(QCoreApplication.translate("GitWidget", u"Push", None))
        self.push_merger_button.setText(QCoreApplication.translate("GitWidget", u"Merge & Push", None))
    # retranslateUi

