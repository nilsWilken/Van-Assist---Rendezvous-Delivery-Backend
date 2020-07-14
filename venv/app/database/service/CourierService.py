from app.database.entity.CourierEntity import Courier
from app.config.DarkMode import DarkMode
from app.config.HelpMode import HelpMode
from app.config.AmbientIntelligenceMode import AmbientIntelligenceMode, IntelligentDrivingMode, TimeBasedDarkMode, SizeDependentWaitingMode, GamificationMode, DynamicContentMode
from app.sql_alchemy_conf  import db
import uuid


"""Fetches the courier by its username"""
def getCourierByUserName(user_name):
    return db.session.query(Courier).filter(Courier.user_name == user_name).first()


"""Fetches the courier by its it"""
def getCourierById(courier_id):
     return db.session.query(Courier).filter(Courier.id == courier_id).first()


"""Validates the user based on its id --> Needed for the firebase authentication"""
def validateCourierById(courier_id):
    courier = db.session.query(Courier).filter(Courier.id == courier_id).first()
    print(courier)
    if courier == None:
        return False
    return True


"""Enables the darkmode"""
def enableDarkMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.dark_mode = DarkMode.ENABLED
        db.session.commit()
    return courier


"""Changes the langugage code"""
def changeLanguage(courier_id, language_code):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.language_code = language_code
        db.session.commit()
    return courier


"""Disables darkmode"""
def disableDarkMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.dark_mode = DarkMode.DISABLED
        db.session.commit()
    return courier


"""Enables helpmode"""
def enableHelpMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.help_mode = HelpMode.ENABLED
        db.session.commit()
    return courier


"""Disables helpmode"""
def disableHelpMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.help_mode = HelpMode.DISABLED
        db.session.commit()
    return courier


"""Updates all verification tokens"""
def updateAllVerificationToken():
    courier_list = db.session.query(Courier).all()
    for courier in courier_list:
        courier.verification_token = str(uuid.uuid4())
    db.session.commit()


def updateVerificationTokenById(courier_id):
    courier_list = db.session.query(Courier).filter(Courier.id == courier_id).all()
    for courier in courier_list:
        courier.verification_token = str(uuid.uuid4())
    db.session.commit()


"""Enables Ambient Intelligence Mode"""
def enableAmbientIntelligenceMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.ambient_intelligence_mode = AmbientIntelligenceMode.ENABLED
        db.session.commit()
    return courier


"""Disables Ambient Intelligence Mode"""
def disableAmbientIntelligenceMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.ambient_intelligence_mode = AmbientIntelligenceMode.DISABLED
        db.session.commit()
    return courier


"""Enable Intelligent Driving Mode"""
def enableIntelligentDrivingMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.intelligent_driving_mode = IntelligentDrivingMode.ENABLED
        db.session.commit()
    return courier


"""Disables Intelligent Driving Mode"""
def disableIntelligentDrivingMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.intelligent_driving_mode = IntelligentDrivingMode.DISABLED
        db.session.commit()
    return courier


"""Enables Size depenendet Waiting Mode"""
def enableSizeDependentWaitingMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.size_dependent_waiting_mode = SizeDependentWaitingMode.ENABLED
        db.session.commit()
    return courier


"""Disables Size depenendet Waiting Mode"""
def disableSizeDependentWaitingMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.size_dependent_waiting_mode = SizeDependentWaitingMode.DISABLED
        db.session.commit()
    return courier


""""Enables Time Based Darkmode"""
def enableTimeBasedDarkMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.time_based_dark_mode = TimeBasedDarkMode.ENABLED
        db.session.commit()
    return courier


"""Disalbes Time Based Darkmode"""
def disableTimeBasedDarkMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.time_based_dark_mode = TimeBasedDarkMode.DISABLED
        db.session.commit()
    return courier


"""Enables Gamification Mode"""
def enableGamificationMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.gamification_mode = GamificationMode.ENABLED
        db.session.commit()
    return courier


"""Disables Gamification Mode"""
def disableGamificationMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.gamification_mode = GamificationMode.DISABLED
        db.session.commit()
    return courier


"""Enable Dynamic Content Mode"""
def enableDynamicContentMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.dynamic_content_mode = DynamicContentMode.ENABLED
        db.session.commit()
    return courier


"""Disable Dynamic Content Mode"""
def disableDynamicContentMode(courier_id):
    courier = getCourierById(courier_id)
    if courier != None:
        courier.dynamic_content_mode = DynamicContentMode.DISABLED
        db.session.commit()
    return courier




