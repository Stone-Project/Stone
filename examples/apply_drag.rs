// stone:job stone:physics.apply_drag
// stone:function apply_drag_rs

#[no_mangle]
pub extern "C" fn apply_drag_rs(velocity: f64, drag: f64, dt: f64) -> f64 {
    velocity * (1.0 - drag * dt)
}
