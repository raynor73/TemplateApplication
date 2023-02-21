package ilapin.template.core.ui.theme

import androidx.compose.material.MaterialTheme
import androidx.compose.material.lightColors
import androidx.compose.runtime.Composable

@Composable
fun AppTheme(content: @Composable () -> Unit) {
    MaterialTheme(
        colors = lightColors(
            primary = Purple40,
            secondary = PurpleGrey40
        ),
        typography = Typography,
        content = content
    )
}