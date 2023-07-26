"""
Tests for AiAsideSummaryConfig class.
"""


from unittest import TestCase
from unittest.mock import patch

from opaque_keys.edx.keys import CourseKey, UsageKey

from cms.lib.ai_aside_summary_config import AiAsideSummaryConfig


class AiAsideSummaryConfigTestCase(TestCase):
    """ Tests for AiAsideSummaryConfig. """
    AI_ASIDE_CONFIG_API_LOCATION = 'ai_aside.config_api.api'
    COURSE_KEY = CourseKey.from_string("course-v1:test+Test+AiAsideSummaryConfigTestCase")
    UNIT_KEY = UsageKey.from_string("block-v1:test+Test+AiAsideSummaryConfigTestCase+type@vertical+block@vertical_test")

    def test_is_enabled(self):
        """
        Check if summary configuration is enabled using the ai_aside lib.
        """
        ai_aside_summary_config = AiAsideSummaryConfig(self.COURSE_KEY)
        with patch(f'{self.AI_ASIDE_CONFIG_API_LOCATION}.is_summary_config_enabled', return_value=True):
            self.assertTrue(ai_aside_summary_config.is_enabled())

        with patch(f'{self.AI_ASIDE_CONFIG_API_LOCATION}.is_summary_config_enabled', return_value=False):
            self.assertFalse(ai_aside_summary_config.is_enabled())

    def test_is_summary_enabled(self):
        """
        Check the summary configuration value for a particular course and an optional unit using the ai_aside lib.
        """
        ai_aside_summary_config = AiAsideSummaryConfig(self.COURSE_KEY)
        with patch(f'{self.AI_ASIDE_CONFIG_API_LOCATION}.is_summary_enabled', return_value=True):
            self.assertTrue(ai_aside_summary_config.is_summary_enabled())

        with patch(f'{self.AI_ASIDE_CONFIG_API_LOCATION}.is_summary_enabled', return_value=False):
            self.assertFalse(ai_aside_summary_config.is_summary_enabled(self.UNIT_KEY))

    def test_set_summary_settings(self):
        """
        Set the summary configuration settings for a particular unit using the ai_aside lib.
        """
        ai_aside_summary_config = AiAsideSummaryConfig(self.COURSE_KEY)
        with patch(f'{self.AI_ASIDE_CONFIG_API_LOCATION}.set_unit_settings', return_value=True):
            self.assertTrue(ai_aside_summary_config.set_summary_settings(self.UNIT_KEY, {}))

        self.assertIsNone(ai_aside_summary_config.set_summary_settings(self.UNIT_KEY))
