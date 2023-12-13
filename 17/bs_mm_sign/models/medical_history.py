# -*- coding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2023 (https://www.bistasolutions.com)
#
##############################################################################

from odoo import fields, models, api


class MedicalHistory(models.Model):
    _name = 'medical.history'
    _description = 'Medical History'

    # General_info
    partner_id = fields.Many2one('res.partner', required=True)
    medical_history_date = fields.Date(default=fields.Date.today, required=True)
    doctor_other = fields.Char()
    phone = fields.Char()
    physical_exam_date = fields.Date()
    pap_smear_date = fields.Date()
    mammogram_date = fields.Date()
    last_menstrual_period = fields.Date()
    prostate_exam = fields.Date()
    other_medical_tests = fields.Text()
    hormone_replacement = fields.Text()
    drug_allergies = fields.Text()
    prescription_medication = fields.Text()
    self_prescribed_medication = fields.Text()

    # Past Medical History
    heart_attack = fields.Boolean(default=False)
    varicose_veins = fields.Boolean(default=False)
    high_cholesterol = fields.Boolean(default=False)
    rheumatic_fever = fields.Boolean(default=False)
    liver_disease = fields.Boolean(default=False)
    kidney_disease = fields.Boolean(default=False)
    depression = fields.Boolean(default=False)
    stroke = fields.Boolean(default=False)
    asthma = fields.Boolean(default=False)
    cancer = fields.Boolean(default=False)
    ulcers = fields.Boolean(default=False)
    gout = fields.Boolean(default=False)
    hepatitis = fields.Boolean(default=False)
    anxiety = fields.Boolean(default=False)
    diseases_of_arteries = fields.Boolean(default=False)
    heart_murmur = fields.Boolean(default=False)
    diabetes_or_blood_sugar = fields.Boolean(default=False)
    arthritis_of_legs_or_arms = fields.Boolean(default=False)
    migraines = fields.Boolean(default=False)
    epilepsy_or_seizures = fields.Boolean(default=False)
    anemia = fields.Boolean(default=False)

    # Family Medical History
    family_heart_attack = fields.Boolean(default=False)
    family_varicose_veins = fields.Boolean(default=False)
    family_high_cholesterol = fields.Boolean(default=False)
    family_rheumatic_fever = fields.Boolean(default=False)
    family_liver_disease = fields.Boolean(default=False)
    family_kidney_disease = fields.Boolean(default=False)
    family_depression = fields.Boolean(default=False)
    family_stroke = fields.Boolean(default=False)
    family_asthma = fields.Boolean(default=False)
    family_cancer = fields.Boolean(default=False)
    family_ulcers = fields.Boolean(default=False)
    family_gout = fields.Boolean(default=False)
    family_hepatitis = fields.Boolean(default=False)
    family_anxiety = fields.Boolean(default=False)
    family_diseases_of_arteries = fields.Boolean(default=False)
    family_heart_murmur = fields.Boolean(default=False)
    family_diabetes_or_blood_sugar = fields.Boolean(default=False)
    family_arthritis_of_legs_or_arms = fields.Boolean(default=False)
    family_migraines = fields.Boolean(default=False)
    family_epilepsy_or_seizures = fields.Boolean(default=False)
    family_anemia = fields.Boolean(default=False)

    # Social History
    diet = fields.Text()
    exercise = fields.Text()
    smoking = fields.Char()
    alcohol = fields.Char()
    caffeine = fields.Char()
    high_stress_level = fields.Text()
    work_activity = fields.Text()
    additional_comments = fields.Text()

    patient_signature = fields.Binary()

    @api.model
    def create(self, values):
        res = super(MedicalHistory, self).create(values)
        res.update_patient_med_tags()
        res.update_family_med_tags()
        return res

    def update_patient_med_tags(self):
        tag_list = []
        if self.heart_attack:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Heart Attack')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.varicose_veins:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Varicose Veins')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.high_cholesterol:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'High Cholesterol')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.rheumatic_fever:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Rheumatic Fever')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.liver_disease:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Liver Disease')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.kidney_disease:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Kidney Disease')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.depression:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Depression')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.stroke:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Stroke')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.asthma:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Asthma')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.cancer:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Cancer')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.ulcers:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Ulcers')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.gout:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Gout')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.hepatitis:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Hepatitis')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.anxiety:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Anxiety')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.diseases_of_arteries:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Diseases Of Arteries')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.heart_murmur:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Heart Murmur')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.diabetes_or_blood_sugar:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Diabetes Or Blood Sugar')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.arthritis_of_legs_or_arms:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Arthritis of legs or arms')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.migraines:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Migraines')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.epilepsy_or_seizures:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Epilepsy Or Seizures')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.anemia:
            tag = self.env['patient.medical.tag'].search([('name', '=', 'Anemia')])
            if tag and tag.id not in self.partner_id.patient_med_tag_ids.ids:
                tag_list.append(tag.id)
        for item in set(tag_list):
            self.partner_id.write({
                'patient_med_tag_ids': [(4, item)]
            })

    def update_family_med_tags(self):
        tag_list = []
        if self.family_heart_attack:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Heart Attack')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_varicose_veins:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Varicose Veins')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_high_cholesterol:
            tag = self.env['family.medical.tag'].search([('name', '=', 'High Cholesterol')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_rheumatic_fever:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Rheumatic Fever')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_liver_disease:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Liver Disease')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_kidney_disease:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Kidney Disease')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_depression:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Depression')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_stroke:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Stroke')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_asthma:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Asthma')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_cancer:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Cancer')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_ulcers:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Ulcers')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_gout:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Gout')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_hepatitis:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Hepatitis')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_anxiety:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Anxiety')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_diseases_of_arteries:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Diseases Of Arteries')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_heart_murmur:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Heart Murmur')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_diabetes_or_blood_sugar:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Diabetes Or Blood Sugar')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_arthritis_of_legs_or_arms:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Arthritis of legs or arms')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_migraines:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Migraines')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_epilepsy_or_seizures:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Epilepsy Or Seizures')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        if self.family_anemia:
            tag = self.env['family.medical.tag'].search([('name', '=', 'Anemia')])
            if tag and tag.id not in self.partner_id.family_med_tag_ids.ids:
                tag_list.append(tag.id)
        for item in set(tag_list):
            self.partner_id.write({
                'family_med_tag_ids': [(4, item)]
            })
